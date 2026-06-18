class Solution{
    public ListNode rotateRight(ListNode head,int k){
   if(head==null || head.next==null) return head;
   int len=1;
   ListNode tail=head;
   while(tail.next!=null){
    len++;
    tail=tail.next;
   }
    k=k%len;
   int s=len-k;
   if (k==0) return head ;
   tail.next=head;
   ListNode temp=head;
   for (int i=1;i<s;i++) {
    temp=temp.next;

   }
   ListNode newhead=temp.next;
   temp.next=null;
 return newhead;
    }
}