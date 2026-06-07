class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0  # number of devices in previous non-empty row
        total = 0
        for row in bank:
            devices = row.count('1')
            if devices:  # if current row has devices
                total += prev * devices  # beams = devices_in_prev_row * devices_in_current_row
                prev = devices  # update prev to current row's device count   
        return total
