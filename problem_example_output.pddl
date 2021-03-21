; X_C
; _O_
; ___

    (define (problem roomba_problemtest)

    	(:domain roomba)

    
        (:objects 
            roomba - roomba
x0y0 - location
x1y0 - location
x2y0 - location
x0y1 - location
x1y1 - location
x2y1 - location
x0y2 - location
x1y2 - location
x2y2 - location
        )

    
        (:init 
            (=(battery-amount roomba) 34)
(=(trash-amount roomba) 0)
(= (steps) 0)
(at roomba x0y0)
(is-empty x0y0)
(is-dirty x0y0)
(is-empty x1y0)
(is-dirty x1y0)
(is-empty x2y0)
(is-charger x2y0)
(is-clean x2y0)
(is-empty x0y1)
(is-dirty x0y1)
(is-clean x1y1)
(is-empty x2y1)
(is-dirty x2y1)
(is-empty x0y2)
(is-dirty x0y2)
(is-empty x1y2)
(is-dirty x1y2)
(is-empty x2y2)
(is-dirty x2y2)
(has-path x0y0 x1y0)
(has-path x0y0 x0y1)
(has-path x1y0 x0y0)
(has-path x1y0 x2y0)
(has-path x1y0 x1y1)
(has-path x2y0 x1y0)
(has-path x2y0 x2y1)
(has-path x0y1 x1y1)
(has-path x0y1 x0y2)
(has-path x0y1 x0y0)
(has-path x1y1 x0y1)
(has-path x1y1 x2y1)
(has-path x1y1 x1y2)
(has-path x1y1 x1y0)
(has-path x2y1 x1y1)
(has-path x2y1 x2y2)
(has-path x2y1 x2y0)
(has-path x0y2 x1y2)
(has-path x0y2 x0y1)
(has-path x1y2 x0y2)
(has-path x1y2 x2y2)
(has-path x1y2 x1y1)
(has-path x2y2 x1y2)
(has-path x2y2 x2y1)
        )

    
        (:goal
            (and
                (is-clean x0y0)
(is-clean x1y0)
(is-clean x2y0)
(is-clean x0y1)
(is-clean x1y1)
(is-clean x2y1)
(is-clean x0y2)
(is-clean x1y2)
(is-clean x2y2)
            )
        )

    
        (:metric minimize
            (steps)
        )
    )

    
