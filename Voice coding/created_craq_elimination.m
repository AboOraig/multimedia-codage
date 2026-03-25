%created_craquing.mp3
 
clc 
close all 
clear all 
%% Pour telecharger et lire un audio dans Matlab 
 
[y Fs]=audioread('C:\Users\abdel\Desktop\created_craquing.mp3'); % old versions of Matlab use wavread('C:\Users\abdel\Desktop\ttttp.wav') instead 
% py=audioplayer(y,Fs);
% play(py)
% stop(py)
%plot(y)
% do the job for each channel separatly then arrange all in a matrix 
x=y(:,1);
x2=y(:,2);
% X=[x1 x2];
% sound(x1,Fs)
z=[];
z(1) = mean([0 0 x(1) x(2) x(3)]);
z(2) = mean([0 x(1) x(2) x(3) x(4)]);
 
for i=3:length(x)-2
    z(i)=mean([x(i-2) x(i- 1) x(i) x(i + 1) x(i + 2)]);
end

ppy=audioplayer(z,Fs);
 play(ppy)
 stop(ppy)
plot(x,'b');
hold on;
plot(z,'r','linewidth',2);
legend('Noisy signal','Filtered signal');
