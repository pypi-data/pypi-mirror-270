#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import subprocess
import argparse
import shutil
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def parse_args(argv):
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        description="Uploads xmls and manifest files for genomes (bins/MAGs) to ENA.")
    
    parser.add_argument('-i', '--input_folder', type=str, help="Root folder for genome upload " +
                        "(default: wd)", default="./")
    parser.add_argument('-l', '--live', action='store_true', help="Select for live upload")
    parser.add_argument('--webin', help='webin id if not Webin-460 or brokering')
    parser.add_argument('--password', help='password if not Webin-460 or brokering')
    parser.add_argument('--post_upload', action='store_true', help="trigger post-upload checks")
    parser.add_argument('--aspera', help='Use aspera for the upload', action='store_true')

    args = parser.parse_args(argv)

    return args

def submit_manifest(manifest_file, upload_dir, genome, live, webin=None, password=None, aspera=False, inputdir=None):
    output_dir = os.path.join(upload_dir, genome + '_out')
    logger.info('Creating submission directory {}'.format(output_dir))
    os.makedirs(output_dir, exist_ok=True)

    bsub_cmd = [
        'bsub',
        '-q', 'production',
        '-g', '/enauploadMAG',
        '-M', '5000',
        '-R "rusage[mem=5000]"',
        '-o', output_dir + '/submit.out',
        '-e', output_dir + '/submit.err'
    ]
    cmd = [
        'ena-webin-cli',
        '-Xms512M', '-Xmx2G', '-Djava.net.preferIPv4Stack=true',
        '-context', 'genome',
        '-userName', webin if webin else os.getenv("ENA_WEBIN")
    ]

    if password is None:
        # The ENV password should be used
        cmd.extend([
            '-passwordEnv ',
            'ENA_WEBIN_PASSWORD'
        ])
        if not os.getenv("ENA_WEBIN_PASSWORD"):
            logger.error("Missing ENA_WEBIN_PASSWORD from the env.")
            sys.exit(1)
    else:
        cmd.extend([
            '-password',
            password
        ])

    cmd.extend([
        '-manifest', manifest_file,
        '-outputDir', output_dir,
        '-submit',
        '-centerName', "EMG"
    ])
    if aspera:
        os.environ["PATH"] += os.pathsep + '/nfs/production/rdf/metagenomics/pipelines/prod/assembly-pipeline/aspera/bin'
        ascp_path = shutil.which("ascp")
        if ascp_path is None:
            logger.info("The ascp binary is missing, it's not possible to use the -ascp option.")
        else:
            cmd.extend(["-ascp", "-inputDir", inputdir])

    if not live:
        cmd.append('-test')
    logger.info('Uploading {} {}'.format("MAG", genome))
    
    env_cp = os.environ.copy()
    p = subprocess.Popen(bsub_cmd + cmd, stdout=subprocess.PIPE, env=env_cp)
    out, err = p.communicate()

def handler(root_folder, live, user, password, aspera, post_upload):
    logger.info("Tracing registered genomes")
    genome_types = ["bin", "MAG"]
    registration_existence = False
    for genome_type in genome_types:
        # Extract registered MAGs/bins
        genome_upload_folder = os.path.join(root_folder, genome_type + "_upload")
        uploadLog = os.path.join(genome_upload_folder, "{}_successful_uploads.txt".format(genome_type))
        failLog = os.path.join(genome_upload_folder, "{}_failed_uploads.txt".format(genome_type))
        registration_filename = "registered_" + genome_type + "s.tsv"
        if not live:
            registration_filename = registration_filename.replace("s.tsv", "s_test.tsv")
        
        registered_genomes_file = os.path.join(genome_upload_folder, registration_filename)
        registered_genomes = []
        if os.path.exists(registered_genomes_file):
            registration_existence = True
            if os.path.exists(uploadLog):
                with open (uploadLog, "r") as f:
                    for line in f:
                        genome_name = line.split('\t')[0]
                        registered_genomes.append(genome_name)
        else:
            continue
        
        ## Generate/recover upload logs
        uploadedMAGs, failedMAGs = [], []
        if not os.path.exists(uploadLog):
            with open(uploadLog, 'w') as f:
                pass
        else:
            with open(uploadLog, "r+") as f:
                for line in f:
                    uploadedMAGs.append(line.rstrip('\n'))

        if not os.path.exists(failLog):
            with open(failLog, 'w') as f:
                pass
        else:
            with open(failLog, "r+") as f:
                for line in f:
                    failedMAGs.append(line.rstrip('\n'))

        ## Retrieve and upload manifests
        if not post_upload:
            manifests = {}
            manifestPaths = glob.glob(os.path.join(genome_upload_folder, "manifests", "*.manifest"))
            for manifest_path in manifestPaths:
                genome_name = manifest_path.split('/')[-1].replace(".manifest", '')
                manifests[genome_name] = manifest_path

            user_config = Path.home() / ".genome_uploader.config.env"
            if user_config.exists():
                logger.debug("Loading the env variables from ".format(str(user_config)))
                load_dotenv(str(user_config))
            logger.info("Found {} manifest files ready for upload.".format(len(manifests)))
            toOmit = []
            for genome in manifests:
                if live:
                    if check_if_already_submitted(genome, genome_upload_folder, uploadedMAGs):
                        toOmit.append(genome)
                    else:
                        submit_manifest(manifests[genome], genome_upload_folder, genome, live, 
                            user, password, aspera, genome_upload_folder)
                else:
                    submit_manifest(manifests[genome], genome_upload_folder, genome, live, 
                        user, password, aspera, genome_upload_folder)
            
            if toOmit:
                logger.info("{} {}s out of {} from folder {} had already been uploaded: "
                    "{}".format(len(toOmit), genome_type, len(manifests), 
                    genome_upload_folder, ','.join(toOmit)))

            successes = len(manifests) - len(toOmit)
            logger.info("Initial manifests: {}\n".format(len(manifests)) +
                "Successfully launched: {}\n".format(successes))
            logger.info("AFTER ALL JOBS HAVE FINISHED, LAUNCH THE POST-UPLOAD CHECK")

        # Post-Upload
        else:
            errorCounter, successCounter, testCounter = 0, 0, 0
            errorLog, successLog = [], []
            dateOfAttempt = ""
            submitFiles = glob.glob(os.path.join(genome_upload_folder, "*", "submit.out"))
            for submitFile in submitFiles:
                success, test = False, False
                MAGname = submitFile.split('/')[-2].replace("_output", "")
                log = MAGname + '\t' + genome_upload_folder
                if not log in uploadedMAGs:
                    with open(submitFile, 'r') as f:
                        for line in f:
                            if "Terminated at" in line:
                                dateOfAttempt = line.rstrip('\n')
                            if "The submission has been completed successfully." in line:
                                success = True
                            if "The TEST submission has been completed successfully" in line:
                                test = True

                    if success:
                        successLog.append(log)
                        successCounter += 1
                    else:
                        if not test:
                            extLog = log + '\t' + dateOfAttempt
                            if not extLog in failedMAGs:
                                errorLog.append(extLog)
                                errorCounter += 1
                        else:
                            testCounter += 1
        
            with open (uploadLog, "a+") as f:
                for elem in successLog:
                    f.write("{}\n".format(elem))
            with open (failLog, "a+") as f:
                for elem in errorLog:
                    f.write("{}\n".format(elem))

            totalLoggingDir = "/homes/germanab/scripts/MAGupload_tests/"
            totalUploadLog = os.path.join(totalLoggingDir, genome_type + "_successful_uploads.txt")
            totalFailLog = os.path.join(totalLoggingDir, genome_type + "_failed_uploads.txt")
            with open (totalUploadLog, "a+") as f:
                for elem in successLog:
                    f.write("{}\n".format(elem))
            with open (totalFailLog, "a+") as f: 
                for elem in errorLog:
                    f.write("{}\n".format(elem))

            logger.info("Found {} submit.out files. ".format(len(submitFiles)))
            logger.info("Newly registered successes: {}, new failures: {}.".format(successCounter, errorCounter)) 
            logger.info("Test submissions (not registered in final logs): {}".format(testCounter))
            logger.info("List of failed uploads can be found at {}".format(failLog))
            logger.info("List of successful uploads can be found at {}".format(uploadLog))
            
    if not registration_existence:
        raise Exception("No registration file found. Check whether you are pointing to the right " +
                        "execution folder. Verify whether upload was in live or test mode. If none " +
                        "of these works, execute genome_uploader again before uploading.")

def check_if_already_submitted(MAGname, uploadDir, uploadLog):
    query = "{}\t{}\n".format(MAGname, uploadDir)
    
    return query in uploadLog

if __name__ == "__main__":
    # credentials and args
    argv = sys.argv[1:]
    args = parse_args(argv)
    webin_username = args.webin if args.webin else None
    webin_password = args.password if args.password else None

    handler(args.input_folder, args.live, webin_username, webin_password, args.aspera, args.post_upload)
    logger.info("Completed.")
