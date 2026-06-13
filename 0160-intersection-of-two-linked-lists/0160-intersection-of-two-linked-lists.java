/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
       int len1=getLength(headA);
       int len2=getLength(headB);
       while(len1>len2){
        headA=headA.next;
        len1--;
       } 
       while(len2>len1){
        headB=headB.next;
        len2--;
       }
       while(headA!=headB){
        headA=headA.next;
        headB=headB.next;
       }
       return headA;


    }
    private int getLength( ListNode h){
        int len=0;
        ListNode curr=h;
        while(curr!=null){
            curr=curr.next;
            len++;
        }
        return len;
    }
}