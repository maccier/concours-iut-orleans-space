package com.maccier.jc1;

import com.maccier.jc1.game.Player;
import com.maccier.jc1.network.packet.*;
import com.maccier.jc1.network.inter.NextTurn;
import com.maccier.jc1.network.inter.ReceiveId;

import java.util.ArrayList;

public class IA  implements NextTurn, ReceiveId{


    public static void main(String[] args){

        Main main = new Main("localhost",25565);

    }

    private String id;
    private Main main;



    private int pm;
    private int t;

    public IA(Main main) {
        this.main = main;

        t = 100;
        pm = 5;
    }


    private void addPowerEngine(int energie){
        this.main.getClient().send(new SendPenginePacket(energie, this.id));
    }

    private void addPowerShield(int energie){
        this.main.getClient().send(new SendPShieldPacket(energie, this.id));
    }

    private void addPowerShootSpeed(int energie){
        this.main.getClient().send(new SendPShootPacket(energie, this.id));
    }

    private void addPowerShoot(int energie){
        this.main.getClient().send(new SendPpuissancePacket(energie, this.id));
    }

    private void stay(){
        this.main.getClient().send(new SendStayPacket(this.id));
    }

    private void shoot(){
        this.main.getClient().send(new SendShootPacket(this.id));
    }

    private void rotate(int rot){
        this.main.getClient().send(new SendRotatePacket(rot, this.id));
    }

    private ArrayList<Player> getOtherPlayer(){
        ArrayList<Player> list = new ArrayList<>();
        for(Player p : this.main.getGame().getPlayers()){
            if(!p.getId().equals(this.id)){
                list.add(p);
            }
        }
        return list;
    }

    private Player getPlayer(){

        for(Player p : this.main.getGame().getPlayers()){
            if(p.getId().equals(this.id)){
               return p;
            }
        }
        return null;
    }

    @Override
    public void play() {

        this.addPowerEngine(1);
        this.rotate(1);
        this.stay();
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }
}

