SERVICE="longshotr"

all:
	gcc -no-pie -Wall -O0 -g -fno-omit-frame-pointer -Wno-deprecated-declarations -D_FORTIFY_SOURCE=0 \
		 -Wno-format -Wno-format-security -z norelro -z execstack \
		-fno-stack-protector -m32 -mpreferred-stack-boundary=2 ${SERVICE}.c -o ${SERVICE} 
clean:	
	rm -fr ${SERVICE} 
	