// Adapted from https://raw.githubusercontent.com/open-ead/sead/master/include/random/seadRandom.h

#pragma once

#include "seadTypes.h"
#include "seadBitUtil.h"

namespace sead
{
/// A fast non-cryptographically secure pseudorandom number generator based on Xorshift128.
class Random
{
public:
    Random(u64 seed) { init(seed); }
    /// @warning Parameters have to be chosen carefully to get a long period. Using this is not
    /// recommended.
    Random(u64 seed_x, u64 seed_y, u64 seed_z, u64 seed_w) { init(seed_x, seed_y, seed_z, seed_w); }

    /// Reset and seed the engine with the specified value.
    void init(u64 seed);
    /// @warning Parameters have to be chosen carefully to get a long period. Using this is not
    /// recommended.
    void init(u64 seed_x, u64 seed_y, u64 seed_z, u64 seed_w);

    /// Generate a random u64.
    u64 getU64();

    void getContext(u64* x, u64* y, u64* z, u64* w) const;

private:
    u64 mX;
    u64 mY;
    u64 mZ;
    u64 mW;
};

}  // namespace sead

