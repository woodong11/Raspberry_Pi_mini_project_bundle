#app.c도 같이 build 하기 위해 수정
KERNEL_HEADERS=/lib/modules/$(shell uname -r)/build
CC = gcc

TARGET := app
obj-m += devicedriver.o

PWD := $(CURDIR)

#make 시 make all 실행
all: driver app

#driver build
driver:
    make -C $(KERNEL_HEADERS) M=$(PWD) modules

#app build
app:
    $(CC) -o $@ $@.c

#driver, app 모두 제거
clean:
    make -C $(KERNEL_HEADERS) M=$(PWD) clean
    rm -f *.o $(TARGET)
