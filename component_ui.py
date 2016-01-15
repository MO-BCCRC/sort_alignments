'''
Created on July 25, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='sort_alignments',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This script is used to sort bam files and generates usable sorted bam files''')

# required arguments
parser.add_argument('--unsorted_bam', metavar='UNSORTED_BAM',
                    help='Name of the bam file')

parser.add_argument('--sorted_bam_prefix', metavar='SORTED_BAM_PREFIX',
                    help='Extension (prefix) of the sorted bam file')

arser.add_argument('--sorted_bam', metavar='SORTED_BAM',
                                       help='Name of the output file')
args, x = parser.parse_known_args()
