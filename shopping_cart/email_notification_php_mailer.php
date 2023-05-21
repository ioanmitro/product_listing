<!-- 
In this example, the sendNotificationEmail function takes the recipient's email address, subject, and message as parameters. It uses the PHPMailer library to configure the SMTP settings, set the sender and recipient details, and send the email.

You'll need to replace the placeholders in the code (smtp.example.com, your_email@example.com, your_email_password) with the actual SMTP server details and email account credentials.

You can call the sendNotificationEmail function in appropriate parts of your application, such as after an order is confirmed or when there is an important account update, to send email notifications to users.

Note: Push notifications require a different approach and usually involve integrating with a push notification service like Firebase Cloud Messaging (FCM) or Apple Push Notification service (APNs). The implementation of push notifications is beyond the scope of this text-based conversation.
-->

<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'path/to/PHPMailer/src/PHPMailer.php';
require 'path/to/PHPMailer/src/Exception.php';
require 'path/to/PHPMailer/src/SMTP.php';

// Function to send an email notification
function sendNotificationEmail($recipientEmail, $subject, $message) {
  $mail = new PHPMailer(true);

  try {
    // SMTP configuration
    $mail->isSMTP();
    $mail->Host = 'smtp.example.com';
    $mail->Port = 587;
    $mail->SMTPAuth = true;
    $mail->Username = 'your_email@example.com';
    $mail->Password = 'your_email_password';
    $mail->SMTPSecure = 'tls';

    // Sender and recipient details
    $mail->setFrom('your_email@example.com', 'Your Name');
    $mail->addAddress($recipientEmail);

    // Email content
    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body = $message;

    // Send the email
    $mail->send();

    return true;
  } catch (Exception $e) {
    // Handle any errors
    return false;
  }
}

// Example usage
$recipientEmail = 'user@example.com';
$subject = 'Order Confirmation';
$message = 'Thank you for your order.';

if (sendNotificationEmail($recipientEmail, $subject, $message)) {
  echo 'Email sent successfully.';
} else {
  echo 'Failed to send email.';
}
?>
