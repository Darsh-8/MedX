<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

class ChatBotController extends Controller
{
    /**
     * Handle incoming chatbot messages.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function handle(Request $request)
    {
        try {
            // Retrieve and sanitize the user's message
            $query = strtolower(trim($request->input('query')));

            // Initialize the reply variable
            $reply = '';

            // Define possible replies based on the user's message
            if (in_array($query, ['hi', 'hello'])) {
                $reply = 'Hello! How can I assist you today?';
            } elseif ($query === 'help') {
                $reply = 'Sure, I can help you with uploading images or answering your queries. Please let me know what you need assistance with.';
            } elseif ($query === 'upload') {
                $reply = 'You can upload your medical images by clicking the upload button in the interface. If you need further assistance, feel free to ask.';
            } elseif (strpos($query, 'diabetes') !== false) {
                $reply = 'Diabetes is a chronic condition that occurs when the body either does not produce enough insulin or cannot effectively use the insulin it produces, leading to high blood sugar levels. If you have more questions about diabetes, please let me know.';
            } elseif (strpos($query, 'hypertension') !== false) {
                $reply = 'Hypertension, commonly known as high blood pressure, is a serious condition that can lead to heart disease, stroke, and other health problems if left untreated. It is important to manage it properly.';
            } elseif (strpos($query, 'asthma') !== false) {
                $reply = 'Asthma is a long-term condition that affects the airways in the lungs, causing them to become inflamed and narrow, which can lead to difficulty in breathing, wheezing, and coughing. If you have asthma, it is crucial to follow your treatment plan.';
            } elseif (strpos($query, 'cancer') !== false) {
                $reply = 'Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells in the body, which can form tumors and affect normal bodily functions. Early detection and treatment are vital.';
            } else {
                $reply = "I'm sorry, I didn't understand that. Can you please rephrase your question or provide more details?";
            }

            // Return the bot's reply as a JSON response
            return Response::json(['answer' => $reply]);

        } catch (\Exception $e) {
            // Log the exception for debugging purposes
            \Log::error('ChatBotController Error: ' . $e->getMessage());

            // Return a generic error message
            return Response::json(['error' => 'Something went wrong. Please try again later.'], 500);
        }
    }
}