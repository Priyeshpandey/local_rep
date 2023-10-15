# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3821/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        new_dominoes = [x for x in dominoes]
        # print(new_dominoes)
        n = len(dominoes)
        left_force = [-1] * n
        right_force = [-1] * n

        if dominoes[0] == 'R':
            right_force[0] = 0

        if dominoes[-1] == 'L':
            left_force[-1] = n-1

        for i in range(1, n - 1):
            if dominoes[n - i - 1] == 'L':
                left_force[n - i - 1] = n - i - 1
            elif dominoes[n - i - 1] == '.' and left_force[n - i] != -1:
                left_force[n - i - 1] = left_force[n - i]

            if dominoes[i] == 'R':
                right_force[i] = i
            elif dominoes[i] == '.' and right_force[i - 1] != -1:
                right_force[i] = right_force[i - 1]

        if right_force[n-2]!=-1:
            right_force[n-1] = right_force[n-2]

        if left_force[1]!=-1:
            left_force[0] = left_force[1]


        for i in range(n):
            if dominoes[i] == '.':
                # check if there exists a left force
                if left_force[i]!=-1:
                    if right_force[i]!=-1:
                        # calculate which force is more powerful
                        dist_L = abs(i-left_force[i])
                        dist_R = abs(i-right_force[i])
                        if dist_L < dist_R:
                            new_dominoes[i] = 'L'
                        elif dist_L > dist_R:
                            new_dominoes[i] = 'R'
                    else:
                        # only left force exists
                        new_dominoes[i] = 'L'
                elif right_force[i]!=-1:
                    # only right force exists
                    new_dominoes[i] = 'R'
        # print(new_dominoes)
        return ''.join(new_dominoes)


if __name__=='__main__':
    sol = Solution()
    dominoes = "...L...R....RR.R....L.....R....R....L..L.R.."
    print(sol.pushDominoes(dominoes))