var curls20lb = {'complete': 0, 'goal': 10}
var curls20lb_trend =  [0, 60, 30, 42, 15, 69, 74]
window.localStorage.setItem('curls20lb', JSON.stringify(curls20lb))
window.localStorage.setItem('curls20lbtrend', JSON.stringify(curls20lb_trend))

var curls30lb = {'complete': 00, 'goal': 10}
var curls30lb_trend =  [0, 10, 46, 20, 59, 90, 73]
localStorage.setItem('curls30lb', JSON.stringify(curls30lb))
localStorage.setItem('curls30lbtrend', JSON.stringify(curls30lb_trend))

var lunges = {'complete': 17, 'goal': 20}
var lunges_trend =  [40, 0, 80, 100, 110, 80, 100]
localStorage.setItem('lunges', JSON.stringify(lunges))
localStorage.setItem('lungestrend', JSON.stringify(lunges_trend))

var timeworkout = {'complete': 20, 'goal': 5}
var timeworkout_trend =  [0, 10, 75, 90, 25, 68, 100]
localStorage.setItem('timeworkout', JSON.stringify(timeworkout))
localStorage.setItem('timeworkouttrend', JSON.stringify(timeworkout_trend))


change_screen(1,  true)
move_progressbar(1)
move_progressbar(2)
move_progressbar(3)
move_progressbar(4)

