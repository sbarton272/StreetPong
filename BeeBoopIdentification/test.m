%% Testing filter on further sounds

clear all
close all

%% Load
F1 = 'Crosswalk1.m4a';
F2 = 'Crosswalk2.m4a';

[y,Fs] = audioread(F2);

%% Visualize

figure;
spectrogram(y,2048,1024,1024*8,Fs,'yaxis');

%% Filter

N = 512;
b1 = fir1(N, [.28e4 / Fs * 2, .29e4 / Fs * 2]);
b2 = fir1(N, [.225e4 / Fs * 2, .235e4 / Fs * 2]);

y1 = filter(b1,1,y);
y2 = filter(b2,1,y);

%% Visualize

figure;
spectrogram(y1 + y2,2048,1024,1024*8,Fs,'yaxis');

%% Energy

S1 = spectrogram(fY1,2048,1024,1024*8,Fs);
S2 = spectrogram(fY2,2048,1024,1024*8,Fs);

S1 = abs(S1);
S2 = abs(S2);

% Threshold power
% TODO max power?
thr = .6;
S1 = S1 .* (S1 > thr);
S2 = S2 .* (S2 > thr);

P1 = sum(S1);
P2 = sum(S2);

%% Filters

% Detection of single pair
D1 = zeros(2,16);
D1(1,1:2) = 1;
D1(2,15:16) = 1;

% Detection of two beeps
D2 = zeros(2,75);
D2(:,1:length(D1)) = D1;
D2(:,75-length(D1)+1:end) = D1;

%% Detection

P = [P1; P2];

[a1,~] = xcorr(P(1,:),D1(1,:));
[a2,lag1] = xcorr(P(2,:),D1(2,:));
acor1 = a1 .* a2;

figure;
plot(lag1,acor1);

[a1,~] = xcorr(P(1,:),D2(1,:));
[a2,lag2] = xcorr(P(2,:),D2(2,:));
acor2 = a1 .* a2;

figure;
plot(lag2,acor2);


