.386
.model flat, c

.code 

; computation  *mult = First * Second
;			   *div = First / Second
;              *res = First % Second 


DivMul proc

	push ebp					; Prolog
	mov ebp, esp
	push ebx

	xor eax, eax
	
	mov ecx, [ebp+8]			; First function argument
	mov edx, [ebp+12]			; Second function argument
    
	or edx, edx					; check if Second arg is == 0  
	jz DivByZero				; if ZF == True jump stright to the epilog 
	
	imul edx, ecx				; edx = 'First' * 'Second'
	
	mov ebx, [ebp+16]			; ebx = 'prod'
    mov [ebx], edx
	
	mov eax, ecx				; eax = 'First'
    cdq							; convert dword to qword edx:eax contains divident
	idiv dword ptr[ebp+12]		; division EAX (AL or AX) on 'Second' function argument EAX = EAX/'Second'
	mov ebx, [ebp+20]			; ebx = 'quo'
    mov [ebx], eax				; *quo = eax
	
	mov ebx, [ebp+24]			; ebx = 'rem'
	mov [ebx], edx				; *rem = edx

	mov eax, 0					; return 0 - all OK
	jmp Epilog					; jump to epilog


DivByZero:				        
	mov eax, 1					; return 1  - NOK

Epilog:							; epilog
	pop ebx 
	pop ebp
	ret

DivMul endp
	   end	