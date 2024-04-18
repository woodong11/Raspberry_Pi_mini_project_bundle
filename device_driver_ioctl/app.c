#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

#define NOD_NAME "/dev/deviceFile"

int cmd;
char buf[30] = "THIS IS APP DATA!";
int main(){
    int fd = open(NOD_NAME, O_RDWR);
    if( fd<0 ){
        printf("ERROR\n");
        exit(1);
    }

		while (1){
				printf("command : 3~6, Age, birth, phone number\n");
				scanf("%d %s", &cmd, &buf);
				
				if (cmd == 3)
					ioctl(fd, _IO(0,3), buf);
				else if (cmd == 4)
					ioctl(fd, _IO(0,4), buf);
				else if (cmd == 5)
					ioctl(fd, _IO(0,5), buf);
				else if (cmd == 6)
					ioctl(fd, _IO(0,6), buf);
				else{
					printf("wrong command");
					break;
				}			
		}

    close(fd);
    return 0;
}
