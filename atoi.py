class Solution:
    def myAtoi(self, s: str) -> int:
        def checkIsInt(self,s):
            # 文字列を前から舐めていき、数字変換が可能な場合は文字列s2に追加、数値変換できない場合には処理を打ち切る
            pointer,s2 = 0,""
            while(pointer < len(s)):
                try:
                    int(s)  # 文字列を実際にint関数で変換してみる
                except ValueError:
                        return int(s2)  # 例外が発生＝変換できないのでFalseを返す
                else:
                    s2 += s[pointer]
                    return True  # 変換できたのでTrueを返す
                pointer += 1
            return int(s2)
            
        # sが2**31乗　ないしは -2の31条だった場合はそれぞれの2の31乗を返す
        if int(s) > 2**31:
            return 2**31
        elif -(2**31) > int(s):
            return -(2**31)
        
        # 前後の空白の文字列を削除しておく
        s = s.split()
        
        # 符号が−の時のみをケアする
        if(s[0] == "-"):
                s.strip("-")
                return -(self.checkIsInt(s))
            
            
        return checkIsInt(self,s)
                
        
        
        
            