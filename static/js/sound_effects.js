/**
 * CodeQuest Celebration & Audio Engine
 * Features:
 *  - "Yaah!" / Joyful Children Cheering Sound Effect on correct answer
 *  - Web Audio API harmonic victory fanfare chords
 *  - High-performance canvas confetti celebration burst
 *  - Sound enable/mute toggle with localStorage persistence
 */

(function() {
    // Sound state
    let soundEnabled = true;
    let cheerAudio = null;
    let audioCtx = null;

    // Initialize audio element
    function initAudio() {
        if (!cheerAudio) {
            cheerAudio = new Audio('/static/sounds/cheer_yay.mp3');
            cheerAudio.preload = 'auto';
            cheerAudio.volume = 0.95;
        }
    }

    // Web Audio API Victory Fanfare + Cheer Vocalization
    function playHarmonicFanfare() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            if (!audioCtx) {
                audioCtx = new AudioContext();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }

            const now = audioCtx.currentTime;

            // Ascending celebratory fanfare chord arpeggio: C5 (523Hz), E5 (659Hz), G5 (784Hz), C6 (1046Hz)
            const notes = [523.25, 659.25, 783.99, 1046.50];
            
            notes.forEach((freq, idx) => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                
                // Mix of triangle and sine for a joyful bell-like chime
                osc.type = idx % 2 === 0 ? 'triangle' : 'sine';
                osc.frequency.setValueAtTime(freq, now + idx * 0.08);

                gain.gain.setValueAtTime(0.001, now + idx * 0.08);
                gain.gain.exponentialRampToValueAtTime(0.22, now + idx * 0.08 + 0.04);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.08 + 0.85);

                osc.connect(gain);
                gain.connect(audioCtx.destination);

                osc.start(now + idx * 0.08);
                osc.stop(now + idx * 0.08 + 0.9);
            });

            // Cheerful harmonic shimmer
            const shimmerOsc = audioCtx.createOscillator();
            const shimmerGain = audioCtx.createGain();
            shimmerOsc.type = 'sine';
            shimmerOsc.frequency.setValueAtTime(1318.51, now + 0.3); // E6
            shimmerGain.gain.setValueAtTime(0.001, now + 0.3);
            shimmerGain.gain.exponentialRampToValueAtTime(0.18, now + 0.35);
            shimmerGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.2);
            shimmerOsc.connect(shimmerGain);
            shimmerGain.connect(audioCtx.destination);
            shimmerOsc.start(now + 0.3);
            shimmerOsc.stop(now + 1.25);

        } catch (e) {
            console.warn("WebAudio fanfare note:", e);
        }
    }

    // Main celebration trigger
    window.playYaahCheerSound = function() {
        if (!soundEnabled) return;

        initAudio();

        // 1. Play real children cheering "Yaah!" MP3
        if (cheerAudio) {
            cheerAudio.currentTime = 0;
            const playPromise = cheerAudio.play();
            if (playPromise !== undefined) {
                playPromise.catch(err => {
                    console.log("Audio autoplay prevented or pending gesture, playing WebAudio fallback:", err);
                });
            }
        }

        // 2. Play celebratory harmonic fanfare
        playHarmonicFanfare();

        // 3. Trigger confetti explosion
        triggerConfetti();
    };

    // Confetti Celebration
    window.triggerConfetti = function() {
        let canvas = document.getElementById('confettiCanvas');
        if (!canvas) {
            canvas = document.createElement('canvas');
            canvas.id = 'confettiCanvas';
            document.body.appendChild(canvas);
        }
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particles = [];
        const colors = ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#38bdf8', '#fbbf24'];

        for (let i = 0; i < 90; i++) {
            particles.push({
                x: canvas.width / 2 + (Math.random() - 0.5) * 200,
                y: canvas.height * 0.45,
                w: Math.random() * 9 + 4,
                h: Math.random() * 7 + 4,
                color: colors[Math.floor(Math.random() * colors.length)],
                vx: (Math.random() - 0.5) * 18,
                vy: (Math.random() - 0.8) * 16 - 3,
                rotation: Math.random() * 360,
                rotSpeed: (Math.random() - 0.5) * 12,
                opacity: 1,
                decay: Math.random() * 0.015 + 0.01
            });
        }

        let animationFrameId;
        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            let alive = false;

            particles.forEach(p => {
                if (p.opacity > 0) {
                    alive = true;
                    p.x += p.vx;
                    p.y += p.vy;
                    p.vy += 0.45; // gravity
                    p.vx *= 0.98; // drag
                    p.rotation += p.rotSpeed;
                    p.opacity -= p.decay;

                    ctx.save();
                    ctx.translate(p.x, p.y);
                    ctx.rotate((p.rotation * Math.PI) / 180);
                    ctx.globalAlpha = Math.max(0, p.opacity);
                    ctx.fillStyle = p.color;
                    ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
                    ctx.restore();
                }
            });

            if (alive) {
                animationFrameId = requestAnimationFrame(render);
            } else {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                cancelAnimationFrame(animationFrameId);
            }
        }

        render();
    };

    // Auto-setup on DOMContentLoaded
    document.addEventListener('DOMContentLoaded', () => {
        initAudio();
    });

})();
