<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flip Card with Tremble Effect</title>
</head>
<body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: Arial, sans-serif;">

    <div style="perspective: 1000px;">
        <input type="checkbox" id="flip-card" style="display: none;">
        <label for="flip-card" style="width: 300px; height: 200px; position: relative; transform-style: preserve-3d; transition: transform 0.6s; cursor: pointer; animation: tremble 0.2s infinite;">
            <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; display: flex; justify-content: center; align-items: center; font-size: 24px; color: white; background-color: #2980b9;">
                Front Side
                <span style="position: absolute; bottom: 10px; font-size: 14px;">Click to Flip</span>
            </div>
            <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; display: flex; justify-content: center; align-items: center; font-size: 24px; color: white; background-color: #e74c3c; transform: rotateY(180deg);">
                Back Side
            </div>
        </label>
    </div>

    <style>
        /* Trembling animation */
        @keyframes tremble {
            0% { transform: translateX(-2px) rotate(0deg); }
            25% { transform: translateX(2px) rotate(-1deg); }
            50% { transform: translateX(-2px) rotate(1deg); }
            75% { transform: translateX(2px) rotate(0deg); }
            100% { transform: translateX(0px) rotate(0deg); }
        }

        /* Trembling for the card initially */
        label {
            animation: tremble 0.2s infinite;
        }

        /* Stop trembling once clicked (after first click) */
        #flip-card:checked + label {
            transform: rotateY(180deg);
            animation: none; /* Stops the trembling animation permanently */
        }

        /* Hover effect remains for hinting interactivity */
        label:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Maintain rotation when flipping between sides */
        #flip-card:checked + label .back {
            transform: rotateY(0deg);
        }
        #flip-card:checked + label .front {
            transform: rotateY(-180deg);
        }
    </style>

</body>
</html>
