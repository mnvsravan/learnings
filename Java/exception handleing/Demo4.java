public class Demo4 {

    public static void main(String[] args) {
        InventoryService service = new InventoryService();

        System.out.println("--- Executing Checkout Attempt ---");
        service.checkoutItem("user_101", "item_999");
    }
}

class InventoryService {

    public void checkoutItem(String userId, String itemId) {
        // 1. Acquire a lock so no other request touches this item simultaneously
        boolean lockAcquired = acquireRedisLock(itemId);

        if (!lockAcquired) {
            System.out.println("Item is currently locked by another request. Please try again.");
            return;
        }

        try {
            // 2. Perform critical business logic
            decrementDatabaseStock(itemId);
            chargeCreditCard(userId);
            System.out.println("Checkout successful!");

        } catch (Exception e) {
            // 3. Handle any unexpected errors (e.g., payment failure or DB error)
            System.out.println("Checkout failed: " + e.getMessage());

        } finally {
            // 4. GUARANTEED CLEANUP: Always release the lock no matter what happens!
            releaseRedisLock(itemId);
        }
    }

    private boolean acquireRedisLock(String itemId) {
        System.out.println("Acquired lock for item: " + itemId);
        return true;
    }

    private void decrementDatabaseStock(String itemId) {
        System.out.println("Updating inventory database...");
        // Simulating an unexpected system failure (e.g., database network timeout)
        throw new RuntimeException("Database timeout during stock update");
    }

    private void chargeCreditCard(String userId) {
        System.out.println("Charging credit card for user: " + userId);
    }

    private void releaseRedisLock(String itemId) {
        System.out.println("Released lock for item: " + itemId);
    }
}
