class Solution:
    def numUniqueEmails(self, emails):
        address_set = set()
        
        for address in emails:
            address = address.split('@')
            local = address[0]
            domain = address[1] 
            local = local.replace('.','')
            if "+" in local:
                local = local[:local.index("+")]
            address_set.add((local, domain))
    
        return len(address_set)