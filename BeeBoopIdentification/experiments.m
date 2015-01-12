%% Determine filters to detect bee-boops

clear all
close all

%% Load
F1 = 'Crosswalk1.m4a';
F2 = 'Crosswalk2.m4a';

% Note Fs the same
[y1,~] = audioread(F1);
[y2,Fs] = audioread(F2);

% Extract beeps, T sec
T = 5;
y3 = y1(1:T*Fs);

T2 = 20;
y4 = y2(1:T2*Fs);

%% Play

% sound(y1,Fs)
% sound(y2,Fs)
% sound(y3,Fs)

%% Spectrogram

figure;
spectrogram(y4,1024*2,1024,1024*8,Fs,'yaxis');

%% Try LPF

b = fir1(256, [.2e4 / Fs * 2, .3e4 / Fs * 2]);

figure;
freqz(b)

fltY = filter(b,1,y3);

%% Spectrogram

figure;
spectrogram(fltY,1024*2,1024,1024*8,Fs,'yaxis');


%% Play

% sound(fltY,Fs)

%% Plot

figure;
subplot(1,2,1);
t = (1:length(fltY)) / Fs;
plot(t, fltY);

subplot(1,2,2);
w = linspace(-Fs,Fs,length(fltY));
plot(w, abs(fftshift(fft(fltY))));

%% Autocorrelation and periodicity - nope nothing obvious

[autocor,lags] = xcorr(fltY,'coeff');

figure;
plot(lags/Fs,autocor);

% About 153 apart

%% Tighter constraints

b1 = fir1(512, [.28e4 / Fs * 2, .29e4 / Fs * 2]);

figure;
freqz(b1)

b2 = fir1(512, [.225e4 / Fs * 2, .235e4 / Fs * 2]);

figure;
freqz(b2)

fY1 = filter(b1,1,y3);
fY2 = filter(b2,1,y3);
fltY2 = fY1 + fY2; 

spectrogram(fltY2,1024*2,1024,1024*8,Fs,'yaxis');

%% Plot

figure;
subplot(1,2,1);
t = (1:length(fltY2)) / Fs;
plot(t, fltY2);

subplot(1,2,2);
w = linspace(-Fs,Fs,length(fltY2));
plot(w, abs(fftshift(fft(fltY2))));

[autocor,lags] = xcorr(fltY,'coeff');

figure;
plot(lags/Fs,autocor);

%% Energy
W = 1024*2;
S1 = spectrogram(fY1,W,1024,1024*8,Fs);
S2 = spectrogram(fY2,W,1024,1024*8,Fs);

S1 = abs(S1);
S2 = abs(S2);

% Threshold power
thr = .6;
S1 = S1 .* (S1 > .6);
S2 = S2 .* (S2 > .6);

P1 = sum(S1);
P2 = sum(S2);
t = linspace(0, length(y3)/Fs, length(P1));
figure;
plot(t,P1,t,P2);

%% Detection

% Detection of single pair

D1 = zeros(2,16);
D1(1,1:2) = 1;
D1(2,15:16) = 1;

P = [P1; P2];

[a1,~] = xcorr(P(1,:),D1(1,:));
[a2,lag1] = xcorr(P(2,:),D1(2,:));
acor1 = a1 .* a2;

figure;
plot(lag1,acor1);

% Detection of two beeps

D2 = zeros(2,75);
D2(:,1:length(D1)) = D1;
D2(:,75-length(D1)+1:end) = D1;

P = [P1; P2];

[a1,~] = xcorr(P(1,:),D2(1,:));
[a2,lag2] = xcorr(P(2,:),D2(2,:));
acor2 = a1 .* a2;

figure;
plot(lag2,acor2);

