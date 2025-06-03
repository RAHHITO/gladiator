player.onChat("spawn", function () {
    for (let index2 = 0; index2 <= good.length; index2++) {
        mobs.spawn(good[index2], pos(5, 0, index2))
    }
    for (let index3 = 0; index3 <= bad.length; index3++) {
        mobs.spawn(bad[index3], pos(5, 0, index3))
    }
})
player.onChat("arena", function () {
    builder.teleportTo(player.position())
    builder.move(BACK, 10)
    builder.move(RIGHT, 10)
    builder.mark()
    for (let index2 = 0; index2 < 4; index2++) {
        builder.move(FORWARD, 20)
        builder.turn(LEFT_TURN)
    }
    builder.raiseWall(POLISHED_ANDESITE, 5)
})
let bad: number[] = []
let good: number[] = []
let index = 0
good = [
CHICKEN,
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
HORSE
]
bad = [
mobs.monster(CREEPER),
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
mobs.monster(BLAZE)
]
