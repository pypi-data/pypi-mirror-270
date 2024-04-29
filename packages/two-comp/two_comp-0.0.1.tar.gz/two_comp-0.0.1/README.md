# two_comp
A library for converting numbers to twos complement values

## Example usage

```
>>> import two_comp
>>> two_comp.twos_8(0xff)
-1
>>> two_comp.twos_8(0xef)
-17
>>> two_comp.twos_16(0xeeee)
-4370
>>> two_comp.twos_16(0xabcd)
-21555
>>> two_comp.twos_32(0xabcdabcd)
-1412584499
>>> two_comp.twos_64(0xabcdabcdabcdabcd)
-6067004223159161907
>>> two_comp.twos_64(0xabcd)
43981
>>> two_comp.twos_8(0xf)
15
```