#lang racket
(print-as-expression #f)
(provide (all-defined-out))

;========;
; Import ;
;========;
; import `throw` and `try_except`.
(require "prob1.rkt")

;===========;
; Problem 2 ;
;===========;
; Task: Implement `eval` using `throw` and `try_except`.
; Note: You can define any other helper functions.

(define (eval1 e)
  (cond
    [(number? e) e]
    [(list? e)
     (let* ([op (first e)]
            [arg1 (eval1 (second e))]
            [arg2 (eval1 (third e ))])
        (cond
          [(eq? op "+") (+ arg1 arg2)]
          [(eq? op "-") (- arg1 arg2)]
          [(eq? op "*") (* arg1 arg2)]
          [(eq? op "/")
           (if (zero? arg2)
             (throw "DivError")
             (/ arg1 arg2))]
          [else (throw "OpError")]))]
    [else (throw "OpError")]))


(define (eval e)
  (try_except
    (lambda () (eval1 e))
    (lambda (msg) (printf "~a\n" msg)))
)



; (eval (list "+" 1 (list "/" 2 (list "-" 3 3))))
; (eval (list "+" 1 (list "#" 2 3)))
; (eval (list "+" 1 (list "*" 2 3)))
