from subprocess import check_call

class OSManager:
    def shutdown(self):
        check_call(['sudo', 'poweroff'])