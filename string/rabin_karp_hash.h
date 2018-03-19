#ifndef RABIN_KARP_HASH_H
#define RABIN_KARP_HASH_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct hash_coefficient {
    int base;
    int modulus;
} hash_coefficent;

typedef long long hash_t;

hash_t rkhash_init(const char* buf, int buf_len, const hash_coefficent* h)
{
    int base = h->base;
    int modulus = h->modulus;

    hash_t curr_hash = 0;

    for (int i = 0; i < buf_len; i++) {
        curr_hash = (curr_hash * base + buf[i]) % modulus;
    }
    return curr_hash;
}

hash_t rkhash_next(hash_t curr_hash, int buf_len, int lhs, int rhs,
    const hash_coefficent* h)
{
    int base = h->base;
    int modulus = h->modulus;

    hash_t offset = lhs;
    for (int i = 0; i < buf_len - 1; i++) {
        offset = offset * base % modulus;
    }

    hash_t next_hash = ((curr_hash + modulus - offset) * base + rhs) % modulus;
    return next_hash;
}

int rk_substring_match(const char* text, const char* pattern,
    const hash_coefficent* h)
{
    int text_len = strlen(text);
    int pattern_len = strlen(pattern);
    hash_t pattern_hash = rkhash_init(pattern, pattern_len, h);

    // current text hash
    hash_t curr_hash = rkhash_init(text, pattern_len, h);

    for (int i = 0; i < text_len - pattern_len; i++) {
        if (curr_hash == pattern_hash) {
            if (strncmp(text + i, pattern, pattern_len) == 0) {
                return i;
            }
        }
        char lhs = text[i];
        char rhs = text[i + pattern_len];
        curr_hash = rkhash_next(curr_hash, pattern_len, lhs, rhs, h);
    }
    return -1;
}

#endif /* RABIN_KARP_HASH_H */
