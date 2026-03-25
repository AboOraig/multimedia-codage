clc
clear all
close all
%Reading the original audio signal
fs=44100;
[y, fs]=audioread('C:\Users\abdel\Desktop\eeeeeee.mp4');%Left_right.mp4
%Playing the original song
p=audioplayer(y,fs);
play(p);
stop(p);
%Adding echo
num=[1,zeros(1,4800),0.8];
den=[1];
x=filter(num,den,y);
p=audioplayer(x,fs);
play(p);
stop(p);
%Removing echo
den=[1,zeros(1,4800),0.8];
num=[1];
r=filter(num,den,x);
p=audioplayer(r,fs);
play(p);
stop(p);
 