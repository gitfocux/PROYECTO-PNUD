#include <16f877a.h>
#fuses XT,NOLVP,NOWDT,PUT
#use delay(clock=20M)
#byte TRISB=0x86
#byte PORTB=0x06
#byte TRISC=0x87
#byte PORTC=0x07
#define B1 PIN_C0
#define B2 PIN_C1
#define V1 PIN_C2
#define V2 PIN_C3
#define V3 PIN_C4
#define V4 PIN_C5
#define BOYA_R1_F PIN_C6
#define BOYA_R1 PIN_C7
#define BOYA_R3 PIN_B1
int c=0;

#INT_EXT
RB0(){
//output_toggle(B1);
////////CIRCULACIÓN DIRECTA //////////
while(input(PIN_B0)==0)
{output_high(V1);
output_high(V2);
output_high(V3);
output_high(V4);}
c=1;
}

#INT_RB
RB4_7(){
/////LENADO INICIAL/////
if(input(PIN_B4)==0)
  {while(1){
     if(input(BOYA_R1)==0)
     {output_high(B1);
     output_low(V2);
     output_low(V1);}
     else{
     output_low(B1);
     output_low(V2);
     output_low(V1);}
     if(input(BOYA_R3)==0)
     {output_high(B2);
     output_low(V3);
     output_low(V4);}
     else{
     output_low(B2);
     output_low(V3);
     output_low(V4);}
     if(input(BOYA_R1_F)==1)
     break;
   }
   c=1;
  }
/////LLENADO DE TODOS LOS TANQUES///// 
if(input(PIN_B5)==0)
   {while(input(BOYA_R1_F)==0)
      {output_high(V1);
      output_high(V3);
      output_high(V4);
      output_low(V2);
      output_low(B1);
      output_low(B2);
      }
      c=1;
   }
}


void main(){
   TRISB=0b11110011;
   PORTB=0x00;
   TRISC=0b11000000;
   PORTC=0x00;
   enable_interrupts(INT_EXT);
   ext_int_edge(h_to_l);
   enable_interrupts(INT_RB);
   enable_interrupts(GLOBAL);
   /*for(;;){
   output_high(V1);
   output_high(V3);
   output_low(B1);
   output_low(B2);
   output_low(V2);
   output_low(V4);
   
      while(input(BOYA_R3)==1)
      {output_high(V4);
      output_high(V1);
      output_high(V3);
      output_low(B1);
      output_low(B2);
      output_low(V2);
      }
      //delay_ms(5000);
   }*/
   for(;;){
   if(c==0)
   {output_low(V1);
   output_low(V3);
   output_low(B1);
   output_low(B2);
   output_low(V2);
   output_low(V4);}
   
   if(c==1)
   {output_high(V1);
   output_high(V3);
   output_low(B1);
   output_low(B2);
   output_low(V2);
   output_low(V4);
   delay_ms(5000);
   c=0;}
   
      while(input(BOYA_R3)==1)
      {output_high(V4);
      output_high(V1);
      output_high(V3);
      output_low(B1);
      output_low(B2);
      output_low(V2);
      }
   }
}

