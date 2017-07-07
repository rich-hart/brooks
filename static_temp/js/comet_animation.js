(function() {
    var actors = {};
    actors.actor_1 = {
        node: document.getElementById("SVG-Circus-43d5e05b-118f-cbbc-bb77-1292f494d601").getElementById("actor_1"),
        type: "circle",
        cx: 50,
        cy: 75,
        dx: 10,
        dy: 23,
        opacity: 1
    };
    var tricks = {};
    tricks.trick_1 = (function(_, a) {
        a = (function(n) {
            return .5 > n ? 2 * n * n : -1 + (4 - 2 * n) * n
        })(a) % 1, 
          a = a * 1 % 1, 
          a = 0 > a ? 1 + a : a;
        var t, n;
        const ANGLE = 135, AMPLITUDE = 30, C1 = 0.0, C2 = .75, C3 = .5;
        // FIXME: Following lines we hacked to get desired commet effect.  Needs to be cleaned
        C1 > a ? 
            (
                t = 2 * a * AMPLITUDE * Math.cos(ANGLE * Math.PI / 180), 
                n = 2 * -a * AMPLITUDE * Math.sin(ANGLE * Math.PI / 180)
            ) 
        : C2 > a ? 
            (
                t = (C3 - 2 * (a - C1)) * AMPLITUDE * Math.cos(ANGLE * Math.PI / 180), 
                n = -(C3 - 2 * (a - C1)) * AMPLITUDE * Math.sin(ANGLE * Math.PI / 180)
            ) 
        : 
            (
                t = 2 * a * AMPLITUDE * Math.cos(ANGLE * Math.PI / 180), 
                n = 2 * -a * AMPLITUDE * Math.sin(ANGLE * Math.PI / 180)

//                t = (-1 * C3 + 2 * (a - C2)) * AMPLITUDE * Math.cos(ANGLE * Math.PI / 180), 
//                n = -(-1 * C3 + 2 * (a - C2)) * AMPLITUDE * Math.sin(ANGLE * Math.PI / 180)
            ), 
            _._tMatrix[4] += t,  _._tMatrix[5] += n;
    });
    tricks.trick_2 = (function(t, i) {
        i = (function(n) {
            return .5 > n ? 2 * n * n : -1 + (4 - 2 * n) * n
        })(i) % 1, i = 0 > i ? 1 + i : i;
        var _ = t.node;
        0.1 >= i ? _.setAttribute("opacity", i * (t.opacity / 0.1)) : i >= 0.93 ? _.setAttribute("opacity", t.opacity - (i - 0.93) * (t.opacity / (1 - 0.93))) : _.setAttribute("opacity", t.opacity)
    });
    var scenarios = {};
    scenarios.scenario_1 = {
        actors: ["actor_1"],
        tricks: [{
            trick: "trick_1",
            start: 0,
            end: 1.00
        }, {
            trick: "trick_2",
            start: 0,
            end: 1
        }],
        startAfter: 0,
        duration: 6000 * 2,
        actorDelay: 300,
        repeat: 0,
        repeatDelay: 1000
    };
    var _reqAnimFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.oRequestAnimationFrame,
        fnTick = function(t) {
            var r, a, i, e, n, o, s, c, m, f, d, k, w;
            for (c in actors) actors[c]._tMatrix = [1, 0, 0, 1, 0, 0];
            for (s in scenarios)
                for (o = scenarios[s], m = t - o.startAfter, r = 0, a = o.actors.length; a > r; r++) {
                    if (i = actors[o.actors[r]], i && i.node && i._tMatrix)
                        for (f = 0, m >= 0 && (d = o.duration + o.repeatDelay, o.repeat > 0 && m > d * o.repeat && (f = 1), f += m % d / o.duration), e = 0, n = o.tricks.length; n > e; e++) k = o.tricks[e], w = (f - k.start) * (1 / (k.end - k.start)), tricks[k.trick] && tricks[k.trick](i, Math.max(0, Math.min(1, w)));
                    m -= o.actorDelay
                }
            for (c in actors) i = actors[c], i && i.node && i._tMatrix && i.node.setAttribute("transform", "matrix(" + i._tMatrix.join() + ")");
            _reqAnimFrame(fnTick)
        };
    _reqAnimFrame(fnTick);
})()
