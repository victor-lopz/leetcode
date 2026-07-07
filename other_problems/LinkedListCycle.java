class ListNode {
    int val;
    ListNode next;
    ListNode() {this.val = 0; this.next = null;}
    ListNode(int val) {this.val = val; this.next = null;}
    ListNode(int val, ListNode next) {this.val = val; this.next = next;}

    boolean hasCycles() {
        ListNode slow = this;
        ListNode fast = slow.next;
        while (fast != null && fast.next != null) {
            if (slow == fast) {return true;}
            fast = fast.next.next;
            slow = slow.next;
        }
        return false;
    }
}

public class LinkedListCycle {
    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2));
        System.out.println(head.hasCycles());
        head.next.next = head;
        System.out.println(head.hasCycles());
    }
}
