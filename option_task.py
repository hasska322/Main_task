def horse_step(x, y, size=5):

    desk = [[0 for _ in range(size)] for _ in range(size)]

    desk[x][y] = 1

    # Возможные ходы
    step_x = [2, 1, -1, -2, -2, -1, 1, 2]
    step_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def can_step(x1, y1, step):
        desk[x1][y1] = step
        done = try_next(x1, y1, step)
        if not done:
            desk[x1][y1] = 0
        return done

    def try_next(x, y, step):

        envir = {'all_steps': False, 'oX': x, 'oY': y, 'counter': -1}

        def next_step():
            x_ = envir['oX']
            y_ = envir['oY']
            while envir['counter'] < 8:
                envir['counter'] += 1
                if envir['counter'] < 8:
                    envir['oX'] = x_ + step_x[envir['counter']]
                    envir['oY'] = y_ + step_y[envir['counter']]
                if (0 <= envir['oX'] < size) and (0 <= envir['oY'] < size) and desk[envir['oX']][envir['oY']] == 0:
                    break
            envir['all_steps'] = envir['counter'] == 8

        if step < size ** 2:
            next_step()
            while not envir['all_steps'] and not can_step(envir['oX'], envir['oY'], step + 1):
                next_step()
            done = not envir['all_steps']
        else:
            done = True
        return done

    try_next(x, y, 1)

    for i in desk:
        print(i)


horse_step(3, 4, 5)
