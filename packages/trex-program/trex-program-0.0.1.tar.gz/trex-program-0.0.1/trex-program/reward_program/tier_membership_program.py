'''
Created on 13 Jun 2021

@author: jacklok
'''
from trexmodel import program_conf
from trexprogram.reward_program.reward_program_base import RewardGiveawayBase

class TierMembershipProgram(RewardGiveawayBase):
    
    def __init__(self, program_configuration, currency=None):
        super(TierMembershipProgram, self).__init__(program_configuration, currency=currency)
        
            
    
    def give(self, customer_acct, transaction_details, reward_set=1): 