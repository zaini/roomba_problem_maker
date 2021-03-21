; XOT__
; OOT__
; O___T

(define (problem roomba_problem7)

    (:domain roomba)

    (:objects
        roomba - roomba
        x0y0 - location
        x1y0 - location
        x2y0 - location
        x3y0 - location
        x4y0 - location
        x0y1 - location
        x1y1 - location
        x2y1 - location
        x3y1 - location
        x4y1 - location
        x0y2 - location
        x1y2 - location
        x2y2 - location
        x3y2 - location
        x4y2 - location
    )

    (:init
        (=(battery-amount roomba) 100)
        (=(trash-amount roomba) 0)
        (= (steps) 0)
        (at roomba x0y0)
        (is-empty x0y0)
        (is-dirty x0y0)
        (is-clean x1y0)
        (is-empty x2y0)
        (is-trashplace x2y0)
        (is-clean x2y0)
        (is-empty x3y0)
        (is-dirty x3y0)
        (is-empty x4y0)
        (is-dirty x4y0)
        (is-clean x0y1)
        (is-clean x1y1)
        (is-empty x2y1)
        (is-trashplace x2y1)
        (is-clean x2y1)
        (is-empty x3y1)
        (is-dirty x3y1)
        (is-empty x4y1)
        (is-dirty x4y1)
        (is-clean x0y2)
        (is-empty x1y2)
        (is-dirty x1y2)
        (is-empty x2y2)
        (is-dirty x2y2)
        (is-empty x3y2)
        (is-dirty x3y2)
        (is-empty x4y2)
        (is-trashplace x4y2)
        (is-clean x4y2)
        (has-path x0y0 x1y0)
        (has-path x0y0 x0y1)
        (has-path x1y0 x0y0)
        (has-path x1y0 x2y0)
        (has-path x1y0 x1y1)
        (has-path x2y0 x1y0)
        (has-path x2y0 x3y0)
        (has-path x2y0 x2y1)
        (has-path x3y0 x2y0)
        (has-path x3y0 x4y0)
        (has-path x3y0 x3y1)
        (has-path x4y0 x3y0)
        (has-path x4y0 x4y1)
        (has-path x0y1 x1y1)
        (has-path x0y1 x0y2)
        (has-path x0y1 x0y0)
        (has-path x1y1 x0y1)
        (has-path x1y1 x2y1)
        (has-path x1y1 x1y2)
        (has-path x1y1 x1y0)
        (has-path x2y1 x1y1)
        (has-path x2y1 x3y1)
        (has-path x2y1 x2y2)
        (has-path x2y1 x2y0)
        (has-path x3y1 x2y1)
        (has-path x3y1 x4y1)
        (has-path x3y1 x3y2)
        (has-path x3y1 x3y0)
        (has-path x4y1 x3y1)
        (has-path x4y1 x4y2)
        (has-path x4y1 x4y0)
        (has-path x0y2 x1y2)
        (has-path x0y2 x0y1)
        (has-path x1y2 x0y2)
        (has-path x1y2 x2y2)
        (has-path x1y2 x1y1)
        (has-path x2y2 x1y2)
        (has-path x2y2 x3y2)
        (has-path x2y2 x2y1)
        (has-path x3y2 x2y2)
        (has-path x3y2 x4y2)
        (has-path x3y2 x3y1)
        (has-path x4y2 x3y2)
        (has-path x4y2 x4y1)
    )

    (:goal
        (and
            (is-clean x0y0)
            (is-clean x1y0)
            (is-clean x2y0)
            (is-clean x3y0)
            (is-clean x4y0)
            (is-clean x0y1)
            (is-clean x1y1)
            (is-clean x2y1)
            (is-clean x3y1)
            (is-clean x4y1)
            (is-clean x0y2)
            (is-clean x1y2)
            (is-clean x2y2)
            (is-clean x3y2)
            (is-clean x4y2)
        )
    )

    (:metric minimize
        (steps)
    )
)