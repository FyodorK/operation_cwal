.386
.model flat, c
.code

; void CalcSum(int a, int b, int c, int* s1, int* s2, int* s3);
; sN = a**N + b**N + c**N


CalcSum proc
		; Prolog
		push ebp
		mov ebp, esp
		sub esp, 12		; allocate 12 bite on the stack for local storage
		push ebx
		push esi
		push edi

		; set function args
		mov eax, [ebp+8]		; a
		mov ebx, [ebp+12]		; b
		mov ecx, [ebp+16]		; c
		mov edx, [ebp+20]		; s1
		mov esi, [ebp+24]		; s2
		mov edi, [ebp+28]		; s3
		
		; calculating s1
		mov [ebp-12], eax       ; local variable
		add [ebp-12], ebx
		add [ebp-12], ecx
		

		; calculating s2

		imul eax, eax			; eax = a*a
		imul ebx, ebx			; ebx = b*b
		imul ecx, ecx			; ecx = c*c

		mov [ebp-8], eax
		add [ebp-8], ebx
		add [ebp-8], ecx
		

		; calculating s3
		imul eax, [ebp+8]		; [ebp+8(12,16)] still contains value of 'a', 'b' and 'c' args, so that is mean that eax = (a*a)*a
		imul ebx, [ebp+12]		; ebx = (b*b)*b
		imul ecx, [ebp+16]		; ecx = (c*c)*c

		mov [ebp-4], eax
		add [ebp-4], ebx
		add [ebp-4], ecx
		

		; output results 
		mov eax, [ebp-12]		; put result value to s1
		mov [edx], eax
		mov eax, [ebp-8]		; put result value to s2
		mov [esi], eax
		mov eax, [ebp-4]		; put result value to s3
		mov [edi], eax

; Epilog
		pop edi
		pop esi
		pop ebx

		mov esp, ebp		; clear local storage
		pop ebp

		ret

CalcSum endp
		end
