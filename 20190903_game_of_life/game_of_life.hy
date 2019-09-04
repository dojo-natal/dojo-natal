(defn is_alive [cell] (if (= cell 1) True False))
(defn check_alive [x y board]
    (try
        (is_alive (get board x y))
    (except [BaseException]
        False)
    (else
        True)
    (finally
        (print "All done"))))

(defn how_many_alive_around [x y board]
    (sum
        (check_alive (+ x 1) y board)
        (check_alive (- x 1) y board)
        (check_alive x (- y 1) board)
        (check_alive x (+ y 1)  board)
        (check_alive (+ x 1) (+ y 1) board)
        (check_alive (- x 1) (- y 1) board)
        (check_alive (+ x 1) (- y 1) board)
        (check_alive (- x 1) (+ y 1) board)))

(defn game_of_life [board]
       (for [x (range (len board))]
        (for [y (range (len board))]
            (if (is_alive (get board x y))
                (how_many_alive_around x y board)))))
