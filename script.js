document.addEventListener("DOMContentLoaded", function() {
    const cells = document.querySelectorAll(".cell");
    const startBtn = document.getElementById("startBtn");
    const restartBtn = document.getElementById("restartBtn");
    const quitBtn = document.getElementById("quitBtn"); // New quit button
    const board = document.getElementById("board");
    let currentPlayer = "X";
    let gameActive = false; // Initialize game as inactive
    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    
    function handleCellClick(e) {
        const cell = e.target;
        const cellIndex = parseInt(cell.id.replace("cell", ""));
        if (cell.textContent === "" && gameActive) {
            cell.textContent = currentPlayer;
            if (checkWin()) {
                showWinner(currentPlayer);
                gameActive = false;
            } else if (checkDraw()) {
                alert("It's a draw!");
                gameActive = false;
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
            }
        }
    }

    function checkWin() {
        return winningCombinations.some(combination => {
            return combination.every(index => {
                return cells[index].textContent === currentPlayer;
            });
        });
    }

    function checkDraw() {
        return [...cells].every(cell => {
            return cell.textContent !== "";
        });
    }

    function resetGame() {
        cells.forEach(cell => {
            cell.textContent = "";
        });
        currentPlayer = "X";
        gameActive = true;
    }

    function showWinner(winner) {
        alert(`${winner} wins!`);
    }

    function startGame() {
        gameActive = true;
        board.classList.remove("hidden");
        restartBtn.classList.remove("hidden");
        quitBtn.classList.remove("hidden"); // Show quit button
        startBtn.classList.add("hidden");
    }

    cells.forEach(cell => {
        cell.addEventListener("click", handleCellClick);
    });

    startBtn.addEventListener("click", startGame);
    restartBtn.addEventListener("click", resetGame);
});
