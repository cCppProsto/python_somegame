import world_items


_map = (
    ('xzABCDEABCDEABCDEABCDEABCDEABut'),
    ('wy             L             vs'),
    ('d                             r'),
    ('a                             o'),
    ('b                             p'),
    ('c                             q'),
    ('d                            Mr'),
    ('aPPP  PPPP  PPPPPPP  PPPP  PPPo'),
    ('b                        N    p'),
    ('c  PPPP  PPPPP    PPPP  PPPP  q'),
    ('d                             r'),
    ('a  PPPPPPPPP    PPPPPPPPPP    o'),
    ('b            P                p'),
    ('c        PPPPPPPPPP           q'),
    ('d                             r'),
    ('a                             o'),
    ('b              T              p'),
    ('c                     T       q'),
    ('d                             r'),
    ('efghijklfghijklFghijklFghijklmn'),
)


class Level1:
    def __init__(self):
        self.__map = []
        self.__background = world_items.Background()
        for j, y in enumerate(_map):
            row = []
            for i, x in enumerate(y):
                pos_x = i * 32
                pos_y = j * 32
                if x == ' ':
                    row.append(world_items.Empty())
                if x == 'P':
                    row.append(world_items.PlatformLong(pos_x, pos_y))
                if x == 'a':
                    row.append(world_items.LeftWallBorderP1(pos_x, pos_y))
                if x == 'b':
                    row.append(world_items.LeftWallBorderP2(pos_x, pos_y))
                if x == 'c':
                    row.append(world_items.LeftWallBorderP3(pos_x, pos_y))
                if x == 'd':
                    row.append(world_items.LeftWallBorderP4(pos_x, pos_y))
                if x == 'e':
                    row.append(world_items.LeftWallBorderDown(pos_x, pos_y))
                if x == 'f':
                    row.append(world_items.BottomWallBorder1(pos_x, pos_y))
                if x == 'g':
                    row.append(world_items.BottomWallBorder2(pos_x, pos_y))
                if x == 'h':
                    row.append(world_items.BottomWallBorder3(pos_x, pos_y))
                if x == 'i':
                    row.append(world_items.BottomWallBorder4(pos_x, pos_y))
                if x == 'j':
                    row.append(world_items.BottomWallBorder5(pos_x, pos_y))
                if x == 'k':
                    row.append(world_items.BottomWallBorder6(pos_x, pos_y))
                if x == 'l':
                    row.append(world_items.BottomWallBorder7(pos_x, pos_y))
                if x == 'm':
                    row.append(world_items.BottomWallBorder8(pos_x, pos_y))
                if x == 'n':
                    row.append(world_items.RightWallBorderDown(pos_x, pos_y))
                if x == 'o':
                    row.append(world_items.RightWallBorder1(pos_x, pos_y))
                if x == 'p':
                    row.append(world_items.RightWallBorder2(pos_x, pos_y))
                if x == 'q':
                    row.append(world_items.RightWallBorder3(pos_x, pos_y))
                if x == 'r':
                    row.append(world_items.RightWallBorder4(pos_x, pos_y))
                if x == 's':
                    row.append(world_items.RightTopWallBorder1(pos_x, pos_y))
                if x == 't':
                    row.append(world_items.RightTopWallBorder2(pos_x, pos_y))
                if x == 'u':
                    row.append(world_items.RightTopWallBorder3(pos_x, pos_y))
                if x == 'v':
                    row.append(world_items.RightTopWallBorder4(pos_x, pos_y))
                if x == 'w':
                    row.append(world_items.LeftTopWallBorder1(pos_x, pos_y))
                if x == 'x':
                    row.append(world_items.LeftTopWallBorder2(pos_x, pos_y))
                if x == 'y':
                    row.append(world_items.LeftTopWallBorder3(pos_x, pos_y))
                if x == 'z':
                    row.append(world_items.LeftTopWallBorder4(pos_x, pos_y))
                if x == 'A':
                    row.append(world_items.TopWallBorder1(pos_x, pos_y))
                if x == 'B':
                    row.append(world_items.TopWallBorder2(pos_x, pos_y))
                if x == 'C':
                    row.append(world_items.TopWallBorder3(pos_x, pos_y))
                if x == 'D':
                    row.append(world_items.TopWallBorder4(pos_x, pos_y))
                if x == 'E':
                    row.append(world_items.TopWallBorder5(pos_x, pos_y))
                if x == 'T':
                    row.append(world_items.WallTorch(pos_x, pos_y))
                if x == 'F':
                    row.append(world_items.BottomWallBorderAnim1(pos_x, pos_y))
                if x == 'L':
                    row.append(world_items.Lights(pos_x, pos_y))
                if x == 'M':
                    row.append(world_items.BigCrate(pos_x, pos_y))
                if x == 'N':
                    row.append(world_items.Door(pos_x, pos_y))

            self.__map.append(row)

    def draw(self):
        self.__background.draw()

        for row in self.__map:
            for cell in row:
                cell.update()
                cell.draw()

    def eventProcessing(self, event):
        pass

    def update(self):
        pass

    def map(self):
        return self.__map
