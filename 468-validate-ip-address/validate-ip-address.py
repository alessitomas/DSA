class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if not queryIP or type(queryIP) != str:
            return "Neither"
            
        
        def valid_ipv4(ip):
            segments = ip.split(".")
            
            if len(segments) != 4:
                return False
            
            
            return all(
                seg.isdigit() and 
                (0 <= int(seg) <= 255) and 
                str(int(seg)) == seg
                for seg in segments
                )
                    
     
                
        def valid_ipv6(ip):
            valid_char = set("abcdef1234567890")
            segments = ip.split(":")
            
            if len(segments) != 8:
                return False
        
            for seg in segments:
                
                if not (1 <= len(seg) <= 4):
                    return False
                
                if not all(c.lower() in valid_char for c in seg):
                    return False
            
            return True
                    
            
                    
        if valid_ipv4(queryIP):
            return "IPv4"
        
        if valid_ipv6(queryIP):
            return "IPv6"
        
        return "Neither"
        
        
        
        