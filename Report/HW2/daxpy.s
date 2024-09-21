.file	"daxpy.cpp"
# Fragment of disassmebly code just showing the daxpy loop

# /filespace/b/bvenkatarama/Desktop/ECE752/HW1/common/HW2/daxpy.cpp:21: 	m5_dump_reset_stats(0,0);
	xorl	%esi, %esi	#
	xorl	%edi, %edi	#
	call	m5_dump_reset_stats@PLT	#
	movapd	.LC5(%rip), %xmm1	#, tmp250
	leaq	75568(%rsp), %r13	#, _185
	movq	%rbx, %rax	# ivtmp.124, ivtmp.129
	.p2align 4,,10
	.p2align 3
.L44:
# /filespace/b/bvenkatarama/Desktop/ECE752/HW1/common/HW2/daxpy.cpp:23: 		Y[i] = alpha*X[i] + Y[i];
	movapd	0(%rbp), %xmm0	# MEM[base: _75, offset: 0B], vect__3.111
	addq	$16, %rax	#, ivtmp.129
	addq	$16, %rbp	#, ivtmp.131
	mulpd	%xmm1, %xmm0	# tmp250, vect__3.111
# /filespace/b/bvenkatarama/Desktop/ECE752/HW1/common/HW2/daxpy.cpp:23: 		Y[i] = alpha*X[i] + Y[i];
	addpd	-16(%rax), %xmm0	# MEM[base: _78, offset: 0B], vect__5.115
# /filespace/b/bvenkatarama/Desktop/ECE752/HW1/common/HW2/daxpy.cpp:23: 		Y[i] = alpha*X[i] + Y[i];
	movaps	%xmm0, -16(%rax)	# vect__5.115, MEM[base: _78, offset: 0B]
	cmpq	%r13, %rax	# _185, ivtmp.129
	jne	.L44	#,
# /filespace/b/bvenkatarama/Desktop/ECE752/HW1/common/HW2/daxpy.cpp:25: 	m5_dump_reset_stats(0,0);
