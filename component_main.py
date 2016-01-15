'''
Created on July 25, 2014
Last update July 25, 2014
@author: raniba
'''

import os

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Sort a bam file using samtools
    '''
    def __init__(self, component_name='sort_alignments', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        Sort a bam file alignment and returns a sorted bam file
        '''

        unsorted_bam = self.args.unsorted_bam

        sorted_bam_prefix = self.args.sorted_bam_prefix
        sorted_bam = self.args.sorted_bam

        #seq1_base = os.path.basename(seq1)
        #seq2_base = os.path.basename(seq2)

        cmd = self.requirements['samtools']

        cmd_args = [
            'sort',
            unsorted_bam,
            sorted_bam.replace(".sorted.bam", sorted_bam_prefix)
        ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    sort_alignments = Component()
    sort_alignments.args = component_ui.args
    sort_alignments.run()

if __name__ == '__main__':

    import component_ui

    _main()
