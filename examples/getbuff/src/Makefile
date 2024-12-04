#SERVICE=getbuff

all:
	clang++ -fsanitize=address,fuzzer getbuff.cc -o getbuff
#all:
#	gcc -m32 -Wall -O0 -g -fno-omit-frame-pointer -Wno-deprecated-declarations -D_FORTIFY_SOURCE=0 \
#		-fno-pie -Wno-format -Wno-format-security -z norelro -z execstack \
#		-fno-stack-protector -mpreferred-stack-boundary=2 ${SERVICE}.c -o ${SERVICE}
#clean:
#	rm -fr ${SERVICE}

