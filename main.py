def on_on_chat():
    index2 = 0
    while index2 <= len(good):
        mobs.spawn(good[index2], pos(5, 0, index2))
        index2 += 1
    index3 = 0
    while index3 <= len(bad):
        mobs.spawn(bad[index3], pos(5, 0, index3))
        index3 += 1
player.on_chat("spawn", on_on_chat)

def on_on_chat2():
    builder.teleport_to(player.position())
    builder.move(BACK, 10)
    builder.move(RIGHT, 10)
    builder.mark()
    for index22 in range(4):
        builder.move(FORWARD, 20)
        builder.turn(LEFT_TURN)
    builder.raise_wall(POLISHED_ANDESITE, 5)
player.on_chat("arena", on_on_chat2)

bad: List[number] = []
good: List[number] = []
index = 0
good = [CHICKEN,
    COW,
    PIG,
    SHEEP,
    WOLF,
    VILLAGER,
    MUSHROOM_COW,
    SQUID,
    RABBIT,
    BAT,
    OCELOT,
    HORSE]
bad = [mobs.monster(CREEPER),
    mobs.monster(SKELETON),
    mobs.monster(ZOMBIE),
    mobs.monster(SPIDER),
    mobs.monster(PIG_ZOMBIE),
    mobs.monster(SLIME),
    mobs.monster(ENDERMAN),
    mobs.monster(SILVERFISH),
    mobs.monster(CAVE_SPIDER),
    mobs.monster(GHAST),
    mobs.monster(LAVA_SLIME),
    mobs.monster(BLAZE)]