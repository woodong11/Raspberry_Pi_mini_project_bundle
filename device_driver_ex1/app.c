//open() , close() syscall을 /dev/deviceFile 로 보내는 app 샘플 코드

#include<stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#define NOD_NAME "/dev/deviceFile"

int main(){
	int fd = open(NOD_NAME, O_RDWR);      // 디바이스 파일 오픈!
	if( fd<0 ){
		printf("ERROR\n");
		exit(1);
	}
	
	printf("device file 읽었어유. 이제 닫아요 \n");

	close(fd);                       // 디바이스 파일 닫기!
		
	return 0;
}
