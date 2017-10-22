package com.maccier.jc1.network.packet;

import com.maccier.jc1.game.Game;
import com.maccier.jc1.network.ClientInfo;
import com.maccier.jc1.network.packet.Packet;

public class SendPenginePacket extends Packet {

    private Game game;
    private int rot;
    private String id;

    public SendPenginePacket(int rot, String id) {
        super("SendPengine");
        this.rot = Math.max(-1, Math.min(1, rot));
        this.id = id;
    }

    @Override
    public synchronized String encode() {
        return this.getIdentifient()+","+this.id+","+rot;
    }

    @Override
    public synchronized void decode(String msg, ClientInfo cli) {

    }

    @Override
    public synchronized Packet reponse(String msg) {
        return null;
    }
}
