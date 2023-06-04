// Adapted from https://raw.githubusercontent.com/open-ead/sead/master/modules/src/random/seadRandom.cpp

#include "seadRandom.h"

namespace sead
{
void Random::init(u64 seed)
{
    const u64 mt_constant = 0x6C0789656C078965;
    mX = mt_constant * (seed ^ (seed >> 30u)) + 1;
    mY = mt_constant * (mX ^ (mX >> 30u)) + 2;
    mZ = mt_constant * (mY ^ (mY >> 30u)) + 3;
    mW = mt_constant * (mZ ^ (mZ >> 30u)) + 4;
}

void Random::init(u64 seed_x, u64 seed_y, u64 seed_z, u64 seed_w)
{
    mX = seed_x;
    mY = seed_y;
    mZ = seed_z;
    mW = seed_w;
}

u64 Random::getU64()
{
    u64 x = mX ^ (mX << 11u);
    mX = mY;
    mY = mZ;
    mZ = mW;
    mW = mW ^ (mW >> 19u) ^ x ^ (x >> 8u);
    return mW;
}

void Random::getContext(u64* x, u64* y, u64* z, u64* w) const
{
    *x = mX;
    *y = mY;
    *z = mZ;
    *w = mW;
}
}  // namespace sead

