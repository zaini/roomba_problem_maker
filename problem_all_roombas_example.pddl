; XXX
; XXX
; XXX

    (define (problem roomba_problemlatest)

    	(:domain roomba)

    
        (:objects 
            x0y0 - location
roomba0 - roomba
x1y0 - location
roomba1 - roomba
x2y0 - location
roomba2 - roomba
x0y1 - location
roomba3 - roomba
x1y1 - location
roomba4 - roomba
x2y1 - location
roomba5 - roomba
x0y2 - location
roomba6 - roomba
x1y2 - location
roomba7 - roomba
x2y2 - location
roomba8 - roomba
        )

    
        (:init 
            (= (steps) 0)
(at roomba0 x0y0)
(is-empty x0y0)
(is-dirty x0y0)
(=(battery-amount roomba0) 100)
(=(trash-amount roomba0) 0)
(at roomba1 x1y0)
(is-empty x1y0)
(is-dirty x1y0)
(=(battery-amount roomba1) 100)
(=(trash-amount roomba1) 0)
(at roomba2 x2y0)
(is-empty x2y0)
(is-dirty x2y0)
(=(battery-amount roomba2) 100)
(=(trash-amount roomba2) 0)
(at roomba3 x0y1)
(is-empty x0y1)
(is-dirty x0y1)
(=(battery-amount roomba3) 100)
(=(trash-amount roomba3) 0)
(at roomba4 x1y1)
(is-empty x1y1)
(is-dirty x1y1)
(=(battery-amount roomba4) 100)
(=(trash-amount roomba4) 0)
(at roomba5 x2y1)
(is-empty x2y1)
(is-dirty x2y1)
(=(battery-amount roomba5) 100)
(=(trash-amount roomba5) 0)
(at roomba6 x0y2)
(is-empty x0y2)
(is-dirty x0y2)
(=(battery-amount roomba6) 100)
(=(trash-amount roomba6) 0)
(at roomba7 x1y2)
(is-empty x1y2)
(is-dirty x1y2)
(=(battery-amount roomba7) 100)
(=(trash-amount roomba7) 0)
(at roomba8 x2y2)
(is-empty x2y2)
(is-dirty x2y2)
(=(battery-amount roomba8) 100)
(=(trash-amount roomba8) 0)
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

    