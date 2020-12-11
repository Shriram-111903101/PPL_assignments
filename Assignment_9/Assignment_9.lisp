"Function in lisp to find nth element from a list of m elements"

(defun nth_ele (N L)
 	(if (null L)
		nil
	(if (zerop N)
		(first L)
		(nth_ele (1- N) (rest L)))))



(princ (nth_ele 5 '(a b c d e f g)))
