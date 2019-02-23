.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]	; 0x2a
	mov	ebx,DWORD PTR [ebp+0xc] ; 0x4f
	mov	eax,ebx					; eax = ebx = 0x4f
	mov	esp,ebp
	pop	ebp	
	ret
