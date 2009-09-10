#!/bin/bash
cd red
cp slice_2_1.png slice_2_1_mini.png
cp slice_4_1.png slice_4_1_mini.png
cp slice_6_1.png slice_6_1_mini.png
cp slice_8_1.png slice_8_1_mini.png
cp slice_2_2.png slice_2_2_mini.png
cp slice_4_2.png slice_4_2_mini.png
cp slice_6_2.png slice_6_2_mini.png
cp slice_8_2.png slice_8_2_mini.png
mogrify -geometry 30% *_mini.png
cd ../tree
cp slice_2_1.png slice_2_1_mini.png
cp slice_4_1.png slice_4_1_mini.png
cp slice_6_1.png slice_6_1_mini.png
cp slice_8_1.png slice_8_1_mini.png
cp slice_2_2.png slice_2_2_mini.png
cp slice_4_2.png slice_4_2_mini.png
cp slice_6_2.png slice_6_2_mini.png
cp slice_8_2.png slice_8_2_mini.png
mogrify -geometry 30% *_mini.png
cd ../sea
cp slice_2_1.png slice_2_1_mini.png
cp slice_4_1.png slice_4_1_mini.png
cp slice_6_1.png slice_6_1_mini.png
cp slice_8_1.png slice_8_1_mini.png
cp slice_2_2.png slice_2_2_mini.png
cp slice_4_2.png slice_4_2_mini.png
cp slice_6_2.png slice_6_2_mini.png
cp slice_8_2.png slice_8_2_mini.png
mogrify -geometry 30% *_mini.png
