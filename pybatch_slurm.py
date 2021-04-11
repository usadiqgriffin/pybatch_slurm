# Author: Usman Sadiq, copy with permissions
# Example usage: python pyconn_xlab start_sub end_sub
import os
import time
import csv
import sys
import argparse
import pprint
import textwrap

def create_sbatch_str(usr_fcn, usr_fcn_args, slurm_p2, hrs):
    """Put the pieces together to make a sbatch command
    """
    timestr = '00-' + '{:02d}'.format(int(hrs)) + ':{:02d}'. \
        format(int(hrs % 1 * 60)) + ':00'
    slurm_pre = "sbatch -p general --nodes=1 --ntasks=1 --mem-per-cpu=1g -t " \
                + timestr + " --wrap='"
    slurm_main = usr_fcn + usr_fcn_args + slurm_p2
    cmd = slurm_pre + slurm_main

    return cmd


def slurm_proc(csvx, start=None, stop=None):
    """Create and submit jobs on slurm cluster according to user provided
    """

    Sids, Cmds = ([] for i in range(2))

    # Open and read first columns of csv
    with open(csvx, 'rt') as f:
        reader = csv.reader(f)
        xls = [row for row in reader]
        print("Reading your csv file, found n={} subjects...\n".format(len(xls)))
        for line in xls:
            Sids.append(line[0])

    # If no subjects are specified, process all subjects in xls file:
    if start < 0:
        start = 0
        stop = len(Sids)

    print('\t N={} subjects to be processed, from {} to {}...\n' \
          .format(stop - start, start, stop - 1))
    print('Following Slurm commands will be used to execute your programs\n')

    # create center of slurm command, according to user input
    # Add -nodesktop etc options for MATLAB

    if 'matlab' in cmd_in:
        usr_fcn = 'matlab -nodesktop -nosplash -singleCompThread -r'
        cmd_pre = " \" " + cmd_in.split()[1] + '('
        cmd_post = ')' + " \" "

    else:
        usr_fcn = cmd_in
        cmd_pre = ' '
        cmd_post = ' '
        slurm_p2 = "'"
    '''
    else:
        raise ValueError('Unspecified or incompatible command; only support 
        MATLAB or bash commands')
    '''
    for off in range(start, stop, batch):
        for subs in range(off, min(off + batch, stop), 1):
            if 'matlab' in cmd_in:
                slurm_p2 = " -logfile log_" + Sids[subs] + "'"

            usr_fcn_args = cmd_pre + str(Sids[subs]) + cmd_post
            cmd = create_sbatch_str(usr_fcn, usr_fcn_args, slurm_p2, hrs)

            print(textwrap.fill(cmd, width=90, initial_indent='\t', \
                                subsequent_indent='\t'))
            Cmds.append(cmd)
            print('\n')

        print('Warning: If you proceed, above code will be executed. '
              'This will cause batch submission of jobs on the Slurm system,'
              'so please double-check details of above program/command. It is '
              'recommended to always start with a small batch to test'
              'your program first \n')
        prompt = 'ARE YOU SURE YOU WANT TO SUBMIT ABOVE JOBS? (1 for YES,' + \
        '0 for NO):'
        num = input(prompt)
        print('\n')
        if int(num):
            for cmd_i in Cmds:
                os.system(cmd_i)
            print('You can view the slurm-jobID.out file to monitor processing')

            if start + batch < stop:
                print('Now waiting {} mins to finish this batch...'. \
                      format(int(wtime / 60.0)))
                time.sleep(wtime)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='PySlurm: A Python module to batch process MATLAB, \
                    FSL using Slurm manager')

    parser.add_argument('-c', '--cmd',
                        action="store", dest="cmd_in", required=True,
                        help="specify command to be run on multiple subjects")
    parser.add_argument('-f', '--file',
                        action="store", dest="file",
                        help="specify csv file to load inputs/subjects from",
                        default="./matlab_test.csv")
    parser.add_argument('--from',
                        action="store", dest="start",
                        help="starting subject number", default="-1")
    parser.add_argument('--to',
                        action="store", dest="stop",
                        help="last subject number", default="-1")
    parser.add_argument('--batch',
                        action="store", dest="batch_size",
                        help="batch size of the files/subjects to process \
                        together", default="30")
    parser.add_argument('--time',
                        action="store", dest="time",
                        help="how long do you expect each batch to take \
                        to process(hours)", default="1.5")

    # Collect user provided options
    options = parser.parse_args()
    csvx = options.file  # csv file containing files/subjects
    st = int(options.start)  # starting subject
    sp = int(options.stop)  # last subject
    cmd_in = options.cmd_in  # command to execute

    batch = int(options.batch_size)  # how many subjects to process \
    # simultaneously, has been tested on longleaf for 1 to 30
    hrs = float(options.time)
    wtime = 3600 * hrs  # how long (secs) to wait after each batch

    # proceed to slurm job creation
    slurm_proc(csvx, start=int(st), stop=int(sp))
