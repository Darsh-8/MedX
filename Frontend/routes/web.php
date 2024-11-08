<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ChatBotController;

Route::get('/', function () {
    return view('index'); // Your main Blade template
});

// Route to handle BotMan requests
Route::post('/botman', [ChatBotController::class, 'handle']);