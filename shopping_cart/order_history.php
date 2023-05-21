# In the below code, the order_history.php page connects to the database, retrieves the order history for the currently # logged-in user, and displays the order details in a table format.

# Make sure to replace the database connection details ($servername, $username, $password, $dbname) with your actual # database credentials.

# We can navigate the user to the "order_history.php" page from your website by adding a link or a button for accessing # the order history feature.


<?php
// Connect to the database
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "order_history";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Retrieve order history for the currently logged-in user
// Replace `user_id` with the actual user ID of the logged-in user
$user_id = 1;

$sql = "SELECT * FROM orders WHERE user_id = $user_id";
$result = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html>
<head>
  <title>Order History</title>
  <style>
    table {
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 8px;
    }
  </style>
</head>
<body>
  <h2>Order History</h2>
  <table>
    <tr>
      <th>Order Date</th>
      <th>Item Name</th>
      <th>Price Code</th>
      <th>Quantity</th>
      <th>Total Cost</th>
    </tr>
    <?php while ($row = mysqli_fetch_assoc($result)): ?>
      <tr>
        <td><?php echo $row['order_date']; ?></td>
        <td><?php echo $row['item_name']; ?></td>
        <td><?php echo $row['price_code']; ?></td>
        <td><?php echo $row['quantity']; ?></td>
        <td><?php echo $row['total_cost']; ?></td>
      </tr>
    <?php endwhile; ?>
  </table>
</body>
</html>

<?php
// Close the database connection
mysqli_close($conn);
?>
